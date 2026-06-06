# uagent — Random User Agent Strings

`uagent` lets you select a random user agent string from a range of categories.
All categories total **10,899** user agent strings.

## Categories

| Category        | Count |
|-----------------|-------|
| `browsers`      | 9420  |
| `mobile`        | 508   |
| `crawlers`      | 442   |
| `email_clients` | 217   |
| `libraries`     | 141   |
| `others`        | 60    |
| `link_checkers` | 34    |
| `offline`       | 34    |
| `validators`    | 17    |
| `consoles`      | 13    |
| `feed_readers`  | 13    |

## Installation

```bash
pip install uagent
```

## Usage

Select a random user agent from all categories:

```python
from uagent import UserAgent

uas = UserAgent()

# Returns a random user agent, selected from all categories
ua = uas.random()
```

Restrict selection to a single category:

```python
# Initialize and select the 'browsers' category
uas = UserAgent('browsers')

# Returns a random user agent from this category
ua = uas.random()
```

Other methods:

```python
uas = UserAgent()

uas.count()                      # Number of user agents in the selected category
uas.all()                        # List of all user agents in the selected category
uas.search('Linux')              # A random user agent containing 'Linux'
uas.search('Linux', rand=False)  # All user agents containing 'Linux'
```

## License

[MIT](LICENSE.txt)
