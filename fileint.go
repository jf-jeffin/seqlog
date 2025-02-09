package main

import (
	"fmt"
	"os"
)

type Lines map[int32]string

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func Readlines(ifile string) Lines {
	d, e := os.Open(ifile)
	check(e)
	defer d.Close()
	dat := make([]byte, 1000000)

	n, e := d.Read(dat)
	check(e)
	var lineno int32 = 1
	fl := make(Lines)
	for i := 0; i < n; i++ {
		buf := string(dat[i])
		for buf != "\n" {
			fl[lineno] += buf
			i++
			buf = string(dat[i])
		}
		lineno++
	}

	return fl
}

func Readfasta(ifile string) Lines {
	fl := make(Lines)
	fi, e := os.Open(ifile)

	check(e)
	defer fi.Close()
	d := make([]byte, 1000000)

	n, e := fi.Read(d)
	check(e)
	var lineno int32 = 1
	var buf2 string
	for i := 0; i < n; i++ {
		buf := string(d[i])
		if buf == ">" || buf2 == ">" {
			for buf != "\n" {
				fl[lineno] += buf
				i++
				buf = string(d[i])
			}
			lineno++
		}
		for buf != ">" && i+1 < n {
			fl[lineno] += buf
			i++

			buf = string(d[i])
			buf2 = buf

		}
		lineno++
	}
	return fl
}

func main() {
	f := Readfasta("rc.fasta")
	fmt.Println(f)

}
