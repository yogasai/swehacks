import json
import requests
from watson_developer_cloud import ToneAnalyzerV3
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge

def main():
	owner = input("Repository owner's name: ")
	repo = input("Repository name: ")

	gitStat(owner, repo)

	watson()


def gitStat(owner, repo):
	stri = ""
	j = 0

	temp_str = 'https://api.github.com/repos/' + owner + '/' + repo + '/issues/comments'

	for k in range(1, 10):

		if len(stri) < 60000:
			par = (('page', k), ('per_page', 100))
			# put github username and password in auth param below
			response = requests.get(temp_str, auth = ('username', 'password'), params = par)

			i = 0

			var = len(json.loads(response.content))
			j = j + var
			while (i < var):
				dict2 = json.loads(response.content)[i]
				comment = dict2['body']
				i = i + 1
				stri = stri + comment


	text_file = open("sent.txt", "w")
	text_file.write(stri)
	text_file.close()

def watson():
	tone_analyzer = ToneAnalyzerV3(
    version ='2017-09-21',
    username ='5c2a9473-aeaf-4a32-a97d-24b898843c4f',
    password ='PN7c4sKsk0OD'
	)

	f = open('sent.txt', 'r')

	stri = ""

	for line in f:
	    stri = stri + line

	text = stri

	content_type = 'application/json'

	color = [0, 0, 0, 0]

	tone = tone_analyzer.tone({"text": text},content_type, sentences = False)

	obj = json.dumps(tone, indent=2)

	l = len(tone['document_tone']['tones'])

	for i in range(0, l):

		if (tone['document_tone']['tones'][i]):

			temp_obj_score = tone['document_tone']['tones'][i]['score']
			temp_obj_id = tone['document_tone']['tones'][i]['tone_id']

			if (temp_obj_id == 'joy'):
				color[0] = temp_obj_score

			elif (temp_obj_id == 'sadness'):
				color[1] = temp_obj_score

			elif (temp_obj_id == 'tentative'):
				color[2] = temp_obj_score

			elif (temp_obj_id == 'analytical'):
				color[3] = temp_obj_score

	output_file("graph.html")

	emotions = ['Joy','Sadness', 'Tentative', 'Analytical']
	repos = ['average', 'you']

	data = {'Emotions' : emotions,
	        'average' : [0.58125,0.532308, 0.717059, 0.696667],
	        'you'   : color
	        }

	source = ColumnDataSource(data = data)

	p = figure(x_range=emotions, y_range = (0, 1), plot_width=500, plot_height = 800, title="Sentiment Averages",
	           toolbar_location=None, tools="")

	p.vbar(x= dodge('Emotions', -0.15, range = p.x_range), top='average', width=0.3, source=source, color = '#c9d9d3', legend = value("Average"))
	p.vbar(x= dodge('Emotions', 0.15, range = p.x_range), top='you', width=0.3, source=source, color = '#718dbf', legend = "Your repo")

	p.y_range.start = 0
	p.x_range.range_padding = 0.1
	p.xaxis.major_label_orientation = 1
	p.xgrid.grid_line_color = None

	show(p)


main()