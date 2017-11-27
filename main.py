def test_get_helloworld():
	assert 'hello world' == get_helloworld()
	
def get_helloworld():
	#print('hello world')
	return 'hello world'
	
def main():
	print(get_helloworld())

if __name__ == '__main__':
	main()
	