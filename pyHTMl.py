from pyhtml import *

t = html(
	head(
		title('Hello'),
		script(src = 'http://path.to/script.js')

		),
	body(
		header("helo")
		)


	)
print(t.render())