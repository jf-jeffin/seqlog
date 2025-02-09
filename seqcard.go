package main

import (
	"fmt"
)

const (
	a = iota
	c
	g
	t
)

type Density map[string]float32
type Loci map[int][3]any
type Frag map[int]string
type Ffrag map[float32]string

func Elecount(seq string) Density {
	ret := make(Density)
	kk := make(map[string]int)
	for i := 0; i < len(seq); i++ {
		te := string(seq[i])
		if _, exi := kk[te]; !exi {
			kk[te] = 1

		} else {
			kk[te] += 1
		}
	}
	ll := float32(len(seq))
	for k, v := range kk {
		v := float32(v)
		ret[k] = (v / ll)
	}
	return ret
}

func seqblock(seq string) (Loci, string, any) {

	site := make(Loci)
	count, max := 1, 0
	var blockStru string
	var gb any

	for i := 0; i+1 < len(seq); i++ {
		if (seq[i] == seq[i+1]) && (seq[i] == seq[i+2]) {
			init := i
			ele := seq[i]
			for ele == seq[i] {
				i++
			}
			length := i - init
			var block = [3]any{init, length, string(ele)}
			site[count] = block
			count += 1
			blockStru += string(ele) + "-"

			if length > max {
				max = length
				gb = block
			}
			i = i - 1
		}

	}
	return site, blockStru, gb
}

func Fragment(seq string, seqdensity Density, elem string) Frag {
	//to fragement seq
	ffrag := make(Frag)

	count := 0
	for i := 0; i < len(seq); i += 4 {
		if i+4 < len(seq) {
			ffrag[count] = seq[i : i+4]

		} else {
			k := len(seq) - i
			ffrag[count] = seq[i : i+k]
		}
		count++
	}
	fco := 1
	fff := make(Frag)

	for i, v := range ffrag {
		den := Elecount(v)

		fff[0] = "Fragne"

		if den[elem] > seqdensity[elem] {

			fff[fco] = v

			for j := i * len(v); j > 0; j-- {
				cff := fff
				fff[fco] = string(seq[j]) + fff[fco]

				if den = Elecount(fff[fco]); den[elem] <= seqdensity[elem] {
					fff = cff

					break
				}
			}
			for k := i*len(v) + len(v); k < len(seq); k++ {
				cdd := fff
				fff[fco] = fff[fco] + string(seq[k])
				if den = Elecount(fff[fco]); den[elem] <= seqdensity[elem] {
					fff = cdd
					break
				}

			}
			fco += 1
		}
	}
	return fff
}

func main() {
	seq := "cccccaaaactgggggtgagtgacgatttttttgaccctgagtag"
	sss := Elecount(seq)
	ll := Fragment(seq, sss, "a")
	fmt.Println(sss["a"])
	fmt.Println(ll)

}
