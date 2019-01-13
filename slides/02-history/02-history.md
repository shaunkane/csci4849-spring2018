slidenumbers: true
autoscale: true

# Fundamentals of Human-Computer Interaction

### CSCI 4849/5849, Shaun Kane, Spring 2018

---
# Today

- Course FAQs
- Mini-design activity
- History of GUIs
- Setup for creating GUIs

---
# FAQs

- Clarification on technology use 
	- in class we'll use HTML/JS/CSS; other tech as needed
- Moodle, Slack, slides, other course resources
- Other questions?

---
# Reading

- Talk with your neighbor about the readings
- What surprised you?
- Other questions / comments?
	- For next time I've posted some discussion questions to consider ahead of time

---
# Some takeaways from reading

- Ubiquitous computing as a concept
- Considering activity and ability

^ Why is Weiser's work so beloved by HCI researchers?
^ Ubicomp focuses on activity - integrate into what people are doing. But it's not really about the gadgets/devices, but about what people need. 
^ Weiser also talked about "calm computing". A big part of this work is in changing the metaphor.

---
# it's not just about disability
## (but disability is important)

---
# Theremin
- [Clara Rockmore playing "The Swan"](https://www.youtube.com/watch?v=pSzTPGlNa5U)

---
# Nintendo Labo

- [Demo video](https://www.youtube.com/watch?v=P3Bd3HUMkyU)
- Great motivating example of what we can do through creative repurposing of existing resources

---
# So what?

- As computer scientists, we get to create interactions
- Often we are assembling interactions from available sensing capabilities
	- Many opportunities to engage in creativity, find new uses for old devices
	- [MacBook accelerometer as lightsaber](https://www.youtube.com/watch?v=qK4AonfnFaM)
	- [Make your own optical theremin](https://www.youtube.com/watch?v=x-Fwjuulb94)

---
# An extremely compressed history of computer interfaces

---
# What should we focus on?

- Understand major points in the evolution of computer interfaces

- Become aware of the underlying and unspoken assumptions that underlie how our technology works

^ A relevant joke, relayed by David Foster Wallace (https://www.1843magazine.com/story/david-foster-wallace-in-his-own-words). Two young fish are swimming around, and run into an older fish. The older fish asks "how's the water?". The younger fish say "what's water?"

- I highly recommend Moggridge's *Designing Interactions* for more history

---
# Key points

- Where did interaction paradigms come from?
- Where do input devices come from?

---
# Influential interactive systems

- Memex concept (1945)
- Sketchpad (1963)
- NLS (1968)
- Xerox Alto (1973), Star (1981)
- Apple Lisa (1983), Macintosh (1984)

---
# MEMory EXtender (Memex, 1945)

- Vannevar Bush, “As we may think,” Atlantic Monthly, 1945 
- Concept sketch for augmenting human capability

---
# Description of the memex in use
"The owner of the memex, let us say, is interested in the origin and properties of the bow and arrow. [...] He has dozens of possibly pertinent books and articles in his memex. First he runs through an encyclopedia, finds an interesting but sketchy article, leaves it projected. Next, in a history, he finds another pertinent item, and ties the two together. Thus he goes, building a trail of many items. Occasionally he inserts a comment of his own, either linking it into the main trail or joining it by a side trail to a particular item. […]"

---
![fit](images/memex-desk.png)

^ Concept sketch of the memex device

---
![fit](images/memex-camera.png)

^ Wearable camera in memex concept! Shades of Google Glass or "life logging camera"

----
# What did computers look like in 1945?

![inline](images/colossus.jpg)

^ Colossus computer, image from https://en.wikipedia.org/wiki/Colossus_computer

---
# Ideas introduced in the memex

- Hypertext
- Bookmarks
- Document annotations
- Sharing annotations (social technology)
- Networked encyclopedias

---
# Sketchpad (1963)

- Interactive drawing tool
- Ivan Sutherland, MIT PhD student
- Used a light pen and an oscilloscope
	- (computer monitors hadn't been invented yet)

---
# First monitor: DEC VT05 (1970)

![inline](images/vt05.png)

^ Worth noting that we did not have CRT monitors until the 1970s.
	
---
# Sketchpad (1963)

![right](images/sketchpad.png)

Video demos: [short](https://www.youtube.com/watch?v=YB3saviItTI), [full](https://www.youtube.com/watch?v=USyoT_Ha_bA)

---
# Contributions of Sketchpad

![right fit](images/sketchpad-2.png)

- Graphical user interface
- Direct manipulation
- CAD concepts
- Constraint solving
- Master objects and instances
- Snapping behavior
- Light pen tracking
- Bimanual interaction

---
# Key idea: Direct manipulation

- In the old world, if you wanted the computer to draw a rectangle, you would have to specify the characteristics of the rectangle 
	- (x, y, width, height)
- Using direct manipulation in Sketchpad, you can draw the rectangle where you want, at the size that you want
- If you want to make it a little larger/smaller, you can drag it to the size you want, rather than guessing

---
# oN-Line System (NLS, 1968)

- Presented by Douglas Engelbart from the Stanford Research Institute
- "The mother of all demos"

---
# NLS (1968)

![right fit](images/nls.png)

- [Demo highlights](https://www.youtube.com/watch?v=VScVgXM7lQQ&list=PLCGFadV4FqU2yAqCzKaxnKKXgnJBUrKTE)
- [Extended, annotated demo](http://www.dougengelbart.org/firsts/dougs-1968-demo.html)
- [Just the input devices](http://www.dougengelbart.org/firsts/dougs-1968-demo.html)

---
# (Some) Contributions from NLS

- Hypertext
- Cut, copy
- File creation
- Direct manipulation
- Mouse, mouse cursor
- Text editor
- Graph editor
- Networking

---
# Dynabook (Alan Kay, 1972)
![fit right](images/Dynabook.png)

- "A personal computer for children of all ages"
- Concept design

---
# Office schematic (Mott and Tesler, 1970s)
![fit right](images/office.png)

"I was in a bar late one afternoon waiting for a friend, doodling on a bar napkin and thinking about this problem. I was just obsessed with this design at the time; I was just consumed by it. I was thinking about what happens in an office. Someone’s got a document and they want to file it, so they walk over to the file cabinet and put it in the file cabinet; or if they want to make a copy of it, they walk over to the copier and they make a copy of it; or they want to throw it away, so they reach under their desk and throw it in the trash can.

I’m sitting there thinking about this and I’m doodling. What ended up on the bar napkin was what Larry and I called the “Office Schematic.” It was a set of icons for a file cabinet, and a copier, or a printer in this case, and a trash can. The metaphor was that entire documents could be grabbed by the mouse and moved around on the screen. We didn’t think about it as a desktop, we thought about it as moving these documents around an office. They could be dropped into a file cabinet, or they could be dropped onto a printer, or they could be dropped into a trashcan."

^ Tim Mott and Larry Tesler made the "office schematic" which became the desktop metaphor

---
# The modern GUI
![fit right](images/alto.png)

- Xerox Alto (1973) 
	- first GUI, WYSIWYG editing, graphics editing  
	- keyboard, 3-button mouse, 5-key chording keyboard
<br><br>
- Xerox Star (1981) - refined, more usable
	- bitmap graphics and text (black text on white background)
	- overlapping windows, desktop metaphor
	- direct manipulation, ethernet networking
	- created through prototyping and user testing

---
# Next steps
![fit right](images/alto.png)

- Apple Lisa (1983)
	- Heavily influenced by Xerox Star
	- Cut, copy, paste; menu bar; desktop metaphor; direct manipulation
	- Selection-action (object-verb) interaction
- Apple Macintosh (1984)
	- First commercial success
	- Good apps: MacWrite and MacPaint
	- Programmers' widget toolbox in ROM
		- Button, checkbox, scrollbar, menu

^ Image: Apple Lisa

---
# Discussion

- So, is the desktop metaphor good?
	- Why is it good?
	- Why is it not good?

---
# A whole world of input devices
![right](images/buxton-collection.png)

- [The Buxton Collection](https://www.microsoft.com/buxtoncollection)
<br><br>
- What about stuff that didn't catch on?
	- e.g. chording keyboard

---
# Disappearing and re-emerging devices
![right](images/twiddler.jpg)

- Sometimes technology needed more time (e.g. iPad became iPhone and then became iPad)
- Sometimes held back by market forces or production (e.g. depth-sensing cameras only became affordable with Microsoft Kinect)
- Sometimes other uses are found (e.g. chording keyboards used in some wearable computing systems)

---
# Design Activity

---
# Design Activity

![fit right](images/kavita.jpg)

- This is [Kavita](https://www.youtube.com/watch?v=P0DzN7oxnX8)
- Kavita has Spinal Muscular Atrophy and uses the Beam robot for telepresence
- What kinds of accessibility challenges would Kavita experience in a class like this?
- Let's brainstorm problems (together) and solutions (with our neighbors)

---
# For next time

- Catch up if you're behind
- Bring a computing device
- We'll be prototyping in HTML, [JQuery](http://jquery.com), and [PureCSS](http://purecss.io); and posting on [Github Pages](http://pages.github.com)
	- It's 1000% OK if you don't feel confident in these things; we will work through it