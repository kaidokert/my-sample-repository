deps = {
  'src/third_party/libsrtp': {
    'url': 'https://chromium.googlesource.com/chromium/deps/libsrtp.git@6252450'
  },
  'src/third_party/flac': {
    'url': 'https://chromium.googlesource.com/chromium/deps/flac.git@b1a01ff'
  },
  'src/third_party/gitpython': {
    'url': 'https://github.com/gitpython-developers/GitPython.git@3.1.45'
  },
  'src/third_party/gitpython/git/ext/gitdb': {
    'url': 'https://github.com/gitpython-developers/gitdb.git@4.0.12'
  },
  'src/third_party/gitpython/git/ext/gitdb/gitdb/ext/smmap': {
    'url': 'https://github.com/gitpython-developers/smmap.git@v5.0.2'
  },
  'src/third_party/depot_tools': {
    'url': 'https://github.com/kaidokert/depot_tools.git@377f55f382fe2b3b4734a94ac3e1b60339695ef8'
  }
}

hooks = [
  {
    'name': 'apatchy',
    'action': ['echo', 'foo']
  },
  {
    'name': 'patch_deps',
    'action': ['python3', 'src/tools/patcher.py']
  }
]