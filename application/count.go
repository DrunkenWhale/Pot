package application

import (
	"bytes"
	"io"
)

func CountFileLine(read io.Reader) (int, int, error) {
	buf := make([]byte, 32*1024)
	line := 0
	blank := 0
	lineSep := []byte{'\n'}
	//blankSep := []byte("\n\n")

	for {
		c, err := read.Read(buf)
		bytes.Contains(buf, []byte{})
		//blank += bytes.Count(buf[:c], blankSep)
		blank +=1
		line += bytes.Count(buf[:c], lineSep)
		switch {
		case err == io.EOF:
			return line, blank, nil

		case err != nil:
			return line, blank, err
		}
	}
}
