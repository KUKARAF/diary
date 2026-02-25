# today

A diary date manager with CLI and Vim integration.

## Installation

```sh
pip install -e '.[cli]'
```

The `cli` extra pulls in [timefhuman](https://github.com/alvinwan/timefhuman) for natural language date parsing.

## Configuration

Config lives at `~/.config/today/config.toml` (created on first run):

```toml
[diary]
directory = "~/vimwiki/diary"
extension = ".md"
```

## CLI

```sh
diary                # today's file (created if it doesn't exist)
diary today          # same as above
diary week           # all existing files for this week (Mon-Sun)
diary month          # all existing files for this month
diary next friday    # file for next friday
diary january 1      # file for january 1
```

### kv_manager

Read and write YAML frontmatter key-value pairs in diary files. File paths are read from stdin.

```sh
diary today | kv_manager set mood 8
diary today | kv_manager get mood        # 8
diary today | kv_manager add mood 1      # 9
diary today | kv_manager sub mood 2      # 7
diary week  | kv_manager get mood        # average across the week
```

## Vim plugin

Add this repo to your Vim runtime path (e.g. via a plugin manager or symlink into `~/.vim/pack/`), then use:

```vim
:Today              " open today's diary file
:Today today        " same as above
:Today week         " open all week files as buffers
:Today month        " open all month files as buffers
:Today next friday  " open next friday's file
```

All returned files are loaded as buffers; the last one is visible. Use `:ls` to see all loaded buffers.
