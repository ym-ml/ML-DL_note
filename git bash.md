1.
	git remote -v  查看所有远程仓库
	git branch -vv  查看当前分支的上游远程仓库
	git branch -u [origin/master] 更改上游
2.
	git push和git pull默认行为不同,git push gitee可以实现,但是git pull gitee不对,必须加上master,即git pull gitee master