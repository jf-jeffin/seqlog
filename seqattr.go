package seqattr

type Keys map[string]string
type Density map[string]float32
type Sequence struct {
	dna string
	aa  string
}

var CompKeys = Keys{
	"g": "c", "c": "g",
	"t": "a", "a": "t",
}

var Rnakey = Keys{
	"g": "c", "c": "g",
	"u": "a", "a": "u",
}

var Nucleotypekey = Keys{
	"g": "u", "c": "u",
	"a": "y", "t": "y",
}

var Hydrophokey = Keys{
	"O": "ACILMFWV",
	"I": "RNDQEK",
	"N": "GHPSTY",
}

var Polarkey = Keys{
	"N": "ACGILMFPWV",
	"U": "NQST", //charged
	"E": "DE",
	"P": "KRH",
}

var Fgstructkey = Keys{
	"C": "D",
	"R": "FWHY",
	"P": "P",
}

type Cardinal struct {
	Length     int
	Compositon Density
}

type AminoEquSeq struct {
	hydropho    string
	groupstruct string
	polar       string
}

type NucEquSeqs struct {
	raw           string
	complementary string
	nucleotypeseq string
	rnaseq        string
}

func (se *NucEquSeqs) Ntransform(h int) string {
	if h == 1 {
		for i := 0; i < len(se.raw); i++ {
			se.complementary += CompKeys[string(se.raw[i])]
		}
		return se.complementary

	} else if h == 2 {

		for i := 0; i < len(se.raw); i++ {
			se.rnaseq += Rnakey[string(se.raw[i])]
		}
		return se.rnaseq
	} else if h == 3 {

		for i := 0; i < len(se.raw); i++ {
			se.nucleotypeseq += Nucleotypekey[string(se.raw[i])]
		}
		return se.nucleotypeseq
	}
	return "a"
}

func (ret *Cardinal) Elecount(seq NucEquSeqs) Density {
	kk := make(Density)
	for i := 0; i < len(seq.raw); i++ {
		te := string(seq.raw[i])
		if _, exi := kk[te]; !exi {
			kk[te] = 1

		} else {
			kk[te] += 1
		}
	}
	ll := float32(len(seq.raw))
	for k, v := range kk {
		kk[k] = (v / ll)
	}

	ret.Compositon = kk
	return ret.Compositon
}
