# <div dir='rtl'>أوامر سطرية ل ROS</div>

<div dir='rtl'>
<ul>
<li>
استدعاء الماستر
</li>
</ul>
</div>

```
roscore
```



## <div dir='rtl'>أوامر خاصة بالنودات</div>

<div dir='rtl'>
<ul>
<li>
لتشغيل نود:
</li>
</ul>
</div>

```
rosrun <package name> <node name>
```

<div dir='rtl'>
<ul>
<li>
لتشغيل نود مع تغيير اسم (name remapping)
</li>
</ul>
</div>

```
rosrun <package name> <node name> <old name>:=<new name>

مثال:

rosrun turtlesim   turtlesim_node   /turtle1/pose:=/position
```

<div dir='rtl'>
<ul>
<li>
عرض قائمة بالنودات
</li>
</ul>
</div>

```
rosnode list
```

<div dir='rtl'>
<ul>
<li>
عرض معلومات عن النود تشمل (مثال سرد التوبيكات المرتبطة مع النود).
</li>
</ul>
</div>

```
rosnode info <topic name>
```

## <div dir='rtl'>أوامر خاصة بالتوبيكات</div>

<div dir='rtl'>
<ul>
<li>
عرض قائمة بالتوبيكات
</li>
</ul>
</div>

```
rostopic list
```