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

## Generating the blog

I use `invoke` with a tasks file as a wrapper for the different workflows one
uses to work on the blog.

# Listing the available commands

You can use `invoke` (or its shorthand `inv`) to list the available generation
options with some documentation for each.

```bash
uv run inv --list
```

Then to run the `build` command:

```bash
uv run inv build
```

# Publishing production blog

```bash
source publish.env  # Contains the required env variables to manage connection
uv run inv preview publish
```
