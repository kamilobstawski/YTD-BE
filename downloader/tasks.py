from pytube import YouTube

from YTD.celery import app


def progress_function(stream, chunk, file_handle, bytes_remaining):
    size = stream.filesize
    app.current_task.update_state(state='PROGRESS',
                                  meta={'current': round((size - bytes_remaining) / 1000000, 3), 'total': round(size / 1000000, 3),
                                        'percent': 100 - (int((float(bytes_remaining) / size) * 100))})


@app.task
def download(url):
    y = YouTube(url, on_progress_callback=progress_function)
    y.streams.first().download()
    return 'Downloading finished'
