import os
import sys

BASEDIR = os.path.dirname(os.path.abspath(__file__))
print("BASEDIR", BASEDIR)
osjoin = os.path.join(BASEDIR, '../third_party/gitpython')
print("depot_tools", osjoin)
sys.path.insert(1, os.path.join(BASEDIR, '../third_party/gitpython'))
sys.path.insert(1, os.path.join(
    BASEDIR, '../third_party/gitpython/git/ext/gitdb'))
sys.path.insert(1, os.path.join(
    BASEDIR, '../third_party/gitpython/git/ext/gitdb/gitdb/ext/smmap'))

from git import Repo

print("okay, patching ready")

repo_root = os.path.join(BASEDIR, '..')

repo = Repo( os.path.join(repo_root, 'third_party/depot_tools'))
for patch in [
    os.path.join(repo_root,'patches/third_party/depot_tools/0001-Test-this.patch')
]:
    repo.git.apply(patch)
