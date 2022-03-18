package application

import (
	"io/fs"
	"os"
	"path/filepath"
	"strings"
)

// GetFiles path must exist and legal
func GetFiles(path string) ([]FileDesc, error) {
	var files []FileDesc
	_ = filepath.Walk(path, func(path string, info fs.FileInfo, err error) error {
		if !info.IsDir() {
			if strings.Contains(path, ".git") {
				return nil
			}

			f, _ := os.Open(path)
			line, blank, _ := CountFileLine(f)
			err := f.Close()
			if err != nil {
				return err
			}

			files = append(files, FileDesc{
				Name: info.Name(),
				Line: line,
				Blank: blank,
			})
		}
		return nil
	})
	return files, nil
}
