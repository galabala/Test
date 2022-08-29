import urllib
import os
class download_file:
	"""
	下载网络文件
	Args: url->网络文件的地址
		dir->下载保存目录
		filename->默认为网络文件的尾缀
		print->打印下载路径&保存路径
	Return: None
	"""
	def __init__(self, url, dir='.', filename='defalut', print=True) -> None:
		if filename == 'defalut':
			filename = os.path.basename(url)

		resp = urllib.request.urlopen(url)
		try:
			with open(os.path.join(dir, filename), 'wb') as f:
				f.write(resp.read())
			if print:
				print('下载成功', url)
				print(os.path.join(dir, filename))
		except Exception as e:
			print('下载失败', e)
if __name__ == '__main__':
	print(os.path.basename())