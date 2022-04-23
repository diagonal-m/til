"""
{
  'Web': {
    'Web技術の基本': ['01_Web技術とは', '02_Webとネットワーク'],
    'a': ['b']
  }
}
"""

from os.path import isdir, join
from glob import glob


def first_contents() -> list:
    """
    1階層目のリストを取得
    """
    path_list = glob('./*')
    return [path for path in path_list if isdir(path)]


def second_contens(first_contents) -> dir:
    """
    {'parents': {
      'child1': [],
      'child2': []
    }}
    """
    second_tree = dict()
    for first_content in first_contents: 
        path_list = glob(first_content + '/*') 
        path_list = [path for path in path_list if isdir(path)]
        tmp_dict = dict() 
        for path in path_list: 
            tmp_dict[path.split('/')[-1]] = [] 
            second_tree[first_content] = tmp_dict

    return second_tree

def third_contens(second_tree) -> dir:
    """
    {'parents': {
        'child1': ['a', 'b'],
        'child2': ['b', 'b']
      }}
    """
    third_tree = second_tree
    for first, second in second_tree.items():
        for second_dir_name in second.keys():
            path = glob(join(first, second_dir_name) + '/*')
            path = [p for p in path if isdir(p)]
            third_tree[first][second_dir_name] = [p.split('/')[-1] for p in path]
    return third_tree

def create_toc(toc_dict):
  """
  READMEをアップデートする
  """
  toc_text = ''
  with open('README.md', 'r') as f:
    md = f.read()
  
  keep_text = md[:md.find('TOC\n')+4]
  print(keep_text)
  for first, seconds in toc_dict.items():
      tmp_text = f"## {first[2:]}\n\n"
      for key, values in seconds.items():
          tmp_text += f"### {key}\n\n"
          for v in values:
            tmp_text += f"- {v}\n"
      toc_text += tmp_text
  print(keep_text + toc_text)
  with open('README.md', 'w') as f:
    f.write(keep_text+toc_text)



if __name__ == '__main__':
    fc = first_contents()
    st = second_contens(fc)
    toc_dict = third_contens(st)
    print(toc_dict)
    create_toc(toc_dict)