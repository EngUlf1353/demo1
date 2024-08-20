import wave
import json
import threading
import time
pause_event = threading.Event()
paused = False
import wave
import pyaudio

# 拾音 / 通过代码 来获取音频
while True:
    def record_audio(filename):
        mic = pyaudio.PyAudio()  # 创建一个是实例化对象
        stream = mic.open(
            format=pyaudio.paInt16,  # 音频样本使用16位整数，更高的音质，常见的音频格式
            channels=1,  # 音频流的声道数量，1是单声道，2是立体声
            rate=44100,  # 每秒钟采集的音频样本数量，44.1Hz，CD的标准采样率
            input=True,  # 指定的流是输入还是输出，
            frames_per_buffer=8192)  # 缓冲区的大小，每次从麦克风读取的音频数据帧数
        # 缓冲区越大，程序相应会稍慢

        print("开始录音...")
        frame = []  # 用于存储录音过程中的音频数据块
        for _ in range(0, int(44100 / 8192 * 5)):  # 以多少的采样率 录制多少秒
            data = stream.read(8192)
            frame.append(data)
        stream.stop_stream()  # 停止音频流
        stream.close()  # 关闭通道
        mic.terminate()  # 终止麦克风

        wf = wave.open(filename, 'wb')  # 写入数据
        wf.setnchannels(1)
        wf.setsampwidth(mic.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frame))
        wf.close()


    record_audio('test.wav')

#拾音结束

    from vosk import Model, KaldiRecognizer
#设置模型路
    model_path = "C:/Users/engul/PycharmProjects/Moss2/vosk-model-small-cn-0.22"

    model=Model(model_path)

    audio_file="C:/Users/engul/PycharmProjects/Moss2/测试/test.wav"

# # 打开音频文件

    wf = wave.open(audio_file, "rb")

#     # 初始化识别器
    recognizer = KaldiRecognizer(model, wf.getframerate())

    # 处理音频流
    result = " "
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            res = recognizer.Result()
            result += json.loads(res)['text'] + " "

#     # 获取到最后的结果部分
    final_res = recognizer.FinalResult()
    result += json.loads(final_res)['text']
    print('识别结果')
    print(result)

    command1 = "吃饭"
    command2 = "天气"
    if command1 in result:

        print("宝宝少吃点，要长胖了你")
        time.sleep(2)

        if command2 in result:
            print("现在杭州的天气很不错，我们出去走走吧")
            time.sleep(2)

    else:
        print("抱歉，没听懂你在说什么")
        time.sleep(2)

#     # 关闭文件
#     # wf.close()
#
#
#
##根据语音输入，返回不同的结果
# #挑战

        # eg1=audioDisposal()
    # 初始化识别器
