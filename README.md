# freeside-pelican

Project that store the markdown files use to generate my blog using pelican.

## Pandoc
### Installing pandoc

```bash
sudo urpmi conda  # Or any available package from your distro
conda create --name pandoc  # Create a conda environment for your pandoc install
conda install --name pandoc pandoc  # Install pandoc in that environment
```

### Using pandoc

You need to enter the conda environment we named `pandoc` to use `pandoc`.

```bash
conda activate pandoc  # Enter in the environment named `pandoc`
```
