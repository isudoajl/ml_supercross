# Important Linux Command for Project

## Command:
```bash
wget --recursive --spider -nv https://vault.racerxonline.com/ 2>&1 | grep -o 'https://[^"]*/venue/[^"]*'

