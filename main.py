import pafy

url = input('Введите URL видео с YouTube: ')

def download(url):
    try:
        video = pafy.new(url)
        streams = video.streams
        available_streams = {}
        count = 1

        for stream in streams:
            print(stream)
            available_streams[count] = stream
            print(f'{count}: {stream}')
            count += 1
        
        stream_count = int(input("Введи номер: "))
        download = streams[stream_count-1].download()
        print('Cкачивание прошло успешно')
    except:
        print('Ссылка не правильная...')

download(url)

