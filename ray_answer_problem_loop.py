import math
import time

while True:
    time.sleep(1)
    problem=input('問題はナニカナ？')

    if(problem == 'OK'):
        print('またね〜')
        break

    elif(problem == '累乗'):
        # 累乗
        num=input('累乗を計算するね。値は？--->')
        index=input('指数は？--->')

        #ans=math.pow(int(num),int(index))
        ans=pow(int(num),int(index))

        print(str(ans))

    elif(problem == '平方根'):
        # 平方根
        root=input('# 平方根を計算するね。値は？--->')

        ans=math.sqrt(int(root))

        print(str(ans))

    elif(problem == '対数'):
        # 対数
        print('対数を求めるよ')
        num=input('真数は？--->')
        e=input('底とする値は？--->')

        ans=math.log(int(num),int(e))

        print(str(ans))

    elif(problem == '角度をラジアンに変換'):
        # 角度の変換
        degree=input('角度の変換をするよ。角度は何度？--->')

        ans=math.radians(int(degree))

        print(str(ans))

    elif(problem == 'ラジアンを角度に変換'):
        radian=input('ラジアンを角度に変換するね。ラジアンは？--->')

        ans=math.degrees(float(radian))

        print(str(ans))

    elif(problem == '三平方の定理'):
        # 三平方の定理
        print('直角三角形の斜辺の長さをもとめるよ')
        x=input('一辺の値は？--->')
        y=input('他の一辺の値は？--->')

        ans=math.hypot(int(x),int(y))

        print(str(ans))

    elif(problem == '三角関数'):
        # sin,cos,tan
        angle=input('sin,cos,tanを求めるね。角度θは？--->')

        sin=math.sin(math.radians(int(angle)))
        cos=math.cos(math.radians(int(angle)))
        tan=math.tan(math.radians(int(angle)))

        print('sin'+angle+'='+str(sin))
        print('cos'+angle+'='+str(cos))
        print('tan'+angle+'='+str(tan))

    else:
        print('???')
