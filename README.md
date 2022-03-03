# 🔌 BoxESP
BoxESP for CSGO based on pygame
This code was based on Tkinter, i redone it in pygame

# ❓ How it Works?
```python
    for Entity in TempEntityList:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        Hp = pm.read_int(Entity + 0x100)
        if not Hp: continue

        my_posRx, my_posRy, my_posRz = get_originpos(Entity)
        state, LegX, LegY = W2S(my_posRx, my_posRy, my_posRz, view)

        my_hedRx, my_hedRy, my_hedRz = get_bonepos(Entity, 8)
        state2, HeadX, HeadY = W2S(my_hedRx, my_hedRy, my_hedRz, view)

        if state and state2:
            Diff = HeadY - LegY
            HeadY += Diff // 5
            Diff = HeadY - LegY
            pygame.draw.line(screen, red, (LegX - Diff // 4, HeadY), (LegX - Diff // 4, LegY))
            pygame.draw.line(screen, red, (LegX + Diff // 4, HeadY), (LegX + Diff // 4, LegY))
            pygame.draw.line(screen, red, (LegX - Diff // 4, HeadY), (LegX + Diff // 4, HeadY))
            pygame.draw.line(screen, red, (LegX - Diff // 4, LegY), (LegX + Diff // 4, LegY))
```

# 📱 Screenshots
![Screenshot_20220303_235452](https://user-images.githubusercontent.com/100863585/156652835-2271c2d6-6968-4982-b6c0-00c886949010.png)
