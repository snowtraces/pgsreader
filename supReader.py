from pgsreader import PGSReader
from imagemaker import make_image
from PIL import ImageOps

pgs = PGSReader('data/001.sup')

count = 0
for ds in pgs.iter_displaysets():
    print(ds.pcs[0].dts)
    if ds.has_image: 
        count = count + 1
        print('pic - 1' + str(count))
        # get Palette Display Segment
        pds = ds.pds[0]
        # get Object Display Segment
        ods = ds.ods[0]

        # get the image!
        img = make_image(ods, pds).convert('RGB')
        img.save('result/image/' + str(count) + '.jpg')
        # img.show()

        # get time when image would have been displayed on screen in milliseconds:
        timestamp_ms = ods.presentation_timestamp
        # print(timestamp_ms)

        print("++++++++++++")