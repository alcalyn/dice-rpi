from adxl345 import ADXL345
import time
  
adxl345 = ADXL345()

dice = [2, 3, 6, 5, 4, 1]
    
while (True):
    axes = adxl345.getAxes(True)
    axes = [axes['x'], axes['y'], axes['z']]
    axesAbs = map(abs, axes)
    maxIndex = axesAbs.index(max(axesAbs))
    orientation = maxIndex

    if axes[maxIndex] < 0:
        orientation += 3

    print 'Dice: %d value: %.3fG' % (dice[orientation], axesAbs[maxIndex])

    time.sleep(0.05)
