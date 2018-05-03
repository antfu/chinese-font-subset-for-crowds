# Chinese font subset generator for [Crowds](https://github.com/ncase/crowds)
This repo is for solving the problem of large size of Chinese font, which is dissused at [here](https://github.com/illyasviel/crowds/pull/15)(in Chinese).

The basic technique is to extract all the Chinese characters appears in `zh-CN.html` file, and make a subset font for them only. This can reduce the font size effectively.

**Downside**: This font become less flexible since it's only have font for the appeared characters. And you many need to generate the font again once you changed the text of `zh-CN.html` file


## Usage
Requirement
- Python 3+

After update the submodule `crowds` then

```
pip install -r pip-requirement.txt
```
```
python ./generate_subset.py
```

Commit the `crowds` and push. It's all you have to do! 🎉
