1.
	git remote -v  查看所有远程仓库
	git branch -vv  查看当前分支的上游远程仓库
	git branch -u [origin/master] 更改上游
2.
	git push和git pull默认行为不同,git push gitee可以实现,但是git pull gitee不对,必须加上master,即git pull gitee master
3.不小心上传了'垃圾'文件到仓库:

*下文是从历史中彻底删除:
	1. 确保 .trash 已添加到 .gitignore
		echo ".trash/" >> .gitignore
	2. 从Git中删除追踪（但保留本地文件）
		git rm -r --cached .trash/
	3. 提交删除
		git commit -m "移除 .trash 目录的版本控制"
	4. 推送到远程
		git push gitee master
	5. 清理本地Git缓存
		git reflog expire --expire=now --all
		git gc --prune=now