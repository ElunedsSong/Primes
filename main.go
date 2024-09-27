package main

import (
	"context"
	"fmt"
	"math/big"
	"os"
	"os/signal"
	"runtime"
	"sort"
	"sync"
	"syscall"
)

type primeRange struct {
	i int
	a *big.Int
	b *big.Int
}

type primeCount struct {
	i     int
	count int
}

type primeCounts []primeCount

func (pc primeCounts) Len() int {
	return len(pc)
}
func (pc primeCounts) Swap(i, j int) {
	pc[i], pc[j] = pc[j], pc[i]
}
func (pc primeCounts) Less(i, j int) bool {
	return pc[i].i < pc[j].i
}

func main() {
	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)

	var wg sync.WaitGroup
	input := make(chan primeRange)
	output := make(chan primeCount)
	result := make(chan []int)
	ctx, cancel := context.WithCancel(context.Background())

	// workers
	for i := 0; i < runtime.GOMAXPROCS(0); i++ {
		wg.Add(1)
		go func() {
			for pr := range input {
				count, ok := predInRange(ctx, pr.a, pr.b, isPrime)
				if ok {
					output <- primeCount{pr.i, count}
				}
			}
			wg.Done()
		}()
	}

	// output collector
	go func() {
		outputs := []primeCount{}
		for pc := range output {
			outputs = append(outputs, pc)
		}

		sort.Sort(primeCounts(outputs))

		var lastIndex int
		prev := outputs[0].i
		for i := 1; i < len(outputs); i++ {
			if outputs[i].i-prev > 1 {
				break
			}
			lastIndex = i
			prev = outputs[i].i
		}

		counts := make([]int, lastIndex+1)
		for i := 0; i <= lastIndex; i++ {
			pc := outputs[i]
			counts[pc.i] = pc.count
		}
		result <- counts
	}()

	// input producer
loop:
	for i := 0; true; i++ {
		a, b := createRange(i)
		fmt.Println(i, a, b)

		select {
		case <-sig:
			break loop
		case input <- primeRange{i, a, b}:
		}
	}

	close(input)
	cancel()
	wg.Wait()
	close(output)
	primeCounts := <-result

	primeRatios := calculateRatios(primeCounts)
	fmt.Println("primes", primeCounts)
	fmt.Println("ratios", primeRatios)

	sum := 0.0
	for i, r := range primeRatios {
		if i == 0 {
			sum += r
			continue
		}

		oldAvg := sum / float64(i+1)
		sum += r
		newAvg := sum / float64(i+2)

		if newAvg >= oldAvg*2 || newAvg <= oldAvg/2 {
			fmt.Println("newAvg", newAvg, "far away from oldAvg", oldAvg, "by factor of", newAvg/oldAvg)
		}
	}
}
