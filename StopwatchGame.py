# template for "Stopwatch: The Game"
import simpleguitk as simplegui

# define global variables
counter=0
score_x=0
score_y=0
score="0/0"
check=True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A="0"
    B="0"
    C="0"
    D=str(t%10)
    seconds=t/10
    if(seconds<60):
        if(seconds<10):
            B=str(0)
            C=str(seconds)
        else:
            B=str(seconds)[0]
            C=str(seconds)[1]
    else:
        minutes=seconds/60
        seconds=seconds%60
        A=str(minutes)
        if(seconds<10):
            B=str(0)
            C=str(seconds)
        else:
            B=str(seconds)[0]
            C=str(seconds)[1]
    return A + ":" + B + C + "." + D
            
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global check
    timer.start()
    check=True

def stop():
    global counter
    global score_x
    global score_y
    global score
    global check
    timer.stop()
    if(check):
        score_y+=1   
        if(counter%10==0):
            score_x+=1
        score=str(score_x) + "/" + str(score_y)
        
    check=False
  
def reset():
    global counter
    global score_x
    global score_y
    global score
    timer.stop()
    counter=0
    score_x=0
    score_y=0
    score="0/0"
    

# define event handler for timer with 0.1 sec interval
def timer():
    global counter
    counter+=1
   
# define draw handler
def draw(canvas):
    global counter
    global score
    canvas.draw_text(format(counter),(150,200),50,"White")
    canvas.draw_text(score,(320,50),25,"Green")
    
# create frame
frame=simplegui.create_frame("Stop Watch",400,400)

# register event handlers
timer=simplegui.create_timer(100,timer)
frame.set_draw_handler(draw)
frame.add_button("Start",start,150)
frame.add_button("Stop",stop,150)
frame.add_button("Reset",reset,150)


# start frame
frame.start()

# Please remember to review the grading rubric
