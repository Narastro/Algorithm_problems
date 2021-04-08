# 2021.04.05. 2018 KAKAO Blind Recruitment #3
# Music

def solution(m, musicinfos):
    # 1. # replace to lowercase
    answer = '(None)'
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    m = m.replace('A#', 'a')
    # 2. for each string
    for music in musicinfos:
        music = music.replace('C#', 'c')
        music = music.replace('D#', 'd')
        music = music.replace('F#', 'f')
        music = music.replace('G#', 'g')
        music = music.replace('A#', 'a')
        # 2-1. Music length, name, sheet
        music_start = music.split(',')[0]
        music_end = music.split(',')[1]
        music_length = (int(music_end.split(':')[0]) - int(music_start.split(':')[0])) * 60 + \
                       (int(music_end.split(':')[1]) - int(music_start.split(':')[1]))
        music_name = music.split(',')[2]
        sheet_music = music.split(',')[3]
        # 2-2. Playing music
        repeat = music_length // len(sheet_music)
        music_listen = sheet_music * repeat + sheet_music[:(music_length % len(sheet_music))]
        # 3. save with music length
        if m in music_listen:
            if answer == '(None)':
                answer = music_name + '//' + str(music_length)
            else:
                if int(answer.split('//')[1]) < music_length:
                    answer = music_name + '//' + str(music_length)
    if answer == '(None)':
        return answer
    else:
        return answer.split('//')[0]
