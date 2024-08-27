from time import sleep

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:

    def __init__(self, users=None, videos=None, current_user=None):
        if users is None:
            self.users = {}
        if videos is None:
            self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):
        if nickname in self.users and hash(password) == self.users[nickname]['password']:
            self.current_user = nickname
            print(f'Добро пожаловать, {nickname}!')
            return True
        else:
            print('Неверное имя пользователя или пароль')
            return False

    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users[nickname] = {}
            self.users[nickname]['password'] = hash(password)
            self.users[nickname]['age'] = age
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')
            return False

    def log_out(self):
        print(f'{self.current_user} покинул нас')
        self.current_user = None
        return True

    def add(self, *videos):
        for video in videos:
            if isinstance(video, Video):
                if self.videos:
                    video_not_exist_flag = True
                    for saved_video in self.videos:
                        if video.title == saved_video.title:
                            video_not_exist_flag = False
                            print('Video title exist:', video)
                            continue

                    if video_not_exist_flag:
                        self.videos.append(video)
                        print('Video added:', video)

                else:
                    self.videos.append(video)
                    print('Video added:', video)
            else:
                print('Error: Not a Video instance')
                return False
        return True

    def get_videos(self, search_str):
        search_result = []
        for video in self.videos:
            if search_str.lower() in video.title.lower():
                search_result.append(video.title)
        if search_result:
            return search_result
        else:
            return 'Video not found'

    def watch_video(self, search_str):

        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return False

        search_result = None
        for video in self.videos:
            if video.title == search_str:
                search_result = video
                continue
        if search_result:
            if self.users[self.current_user]['age'] >= 18 and search_result.adult_mode:
                for timer in range(search_result.duration):
                    search_result.time_now = timer + 1
                    print(search_result.time_now)
                    sleep(1)
                search_result.time_now = 0
                print('Конец видео')
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')


        else:
            return 'Video not found'


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

ur.log_out()
ur.log_in('vasya_pupkin', 'lolkekcheburek')
