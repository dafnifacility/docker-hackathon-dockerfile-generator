test:
	docker run -it \
		-e GIT_URL=https://github.com/alexm-stfc/dafni-example-models \
		-e SUBFOLDER=uk-climate-analysis \
		test
