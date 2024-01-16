import setuptools

setuptools.setup(
    name="git-tools",
    version="0.1.0",
    py_modules=["git_filter_blobs", "join_git_repos", "make_submodule_repo"],
    entry_points={
        "console_scripts": [
            "git-filter-blobs=git_filter_blobs:main",
            "git-join-git-repos=join_git_repos:main",
            "git-make-submodule-repo=make_submodule_repo:main",
        ]
    },
)
