build:
	docker build -t test .
test:
	docker run -it \
		-e GIT_URL=https://github.com/alexm-stfc/dafni-example-models \
		-e SUBFOLDER=uk-climate-analysis \
		-v /Users/alexander.manning/projects/DAFNI/test-data:/data \
		test
