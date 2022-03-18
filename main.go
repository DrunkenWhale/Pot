package main

import (
	"bytes"
	"fmt"
	"io"
	"io/fs"
	"os"
	"path/filepath"
)

func main() {
	currentPath, err := os.Getwd()
	if err != nil {
		fmt.Println("This path is unreached")
		return
	}
	wantedPath := os.Args[1]
	path := currentPath + string(os.PathSeparator) + wantedPath
	_, err = os.Stat(path)
	if err != nil {
		fmt.Println("Unknown Path")
		return
	}
	files, _ := GetFiles(path)
	for _, file := range files {
		fmt.Println(file)
	}
}

type FileDesc struct {
	name string
	line int
}

// GetFiles path must exist and legal
func GetFiles(path string) ([]FileDesc, error) {
	var files []FileDesc
	filepath.Walk(path, func(path string, info fs.FileInfo, err error) error {

		if !info.IsDir() {
			f, _ := os.Open(path)
			line, _ := CountFileLine(f)
			f.Close()

			files = append(files, FileDesc{
				name: info.Name(),
				line: line,
			})
		}
		return nil
	})
	return files, nil
}

func CountFileLine(read io.Reader) (int, error) {
	buf := make([]byte, 32*1024)
	count := 0
	lineSep := []byte{'\n'}

	for {
		c, err := read.Read(buf)
		count += bytes.Count(buf[:c], lineSep)

		switch {
		case err == io.EOF:
			return count, nil

		case err != nil:
			return count, err
		}
	}
}
