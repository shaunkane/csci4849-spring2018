# Assignment 1: GUI Prototyping

Due **Wednesday January 30 at 3pm.** It's OK to discuss this project with others as you work on it and to get help if you're stuck, but each person needs to complete this assignment.

In this assignment, we will code up our first user interface. For this activity, and throughout the course, we will be building user interfaces in HTML (Hypertext Markup Language), CSS (Cascading Style Sheets), and JavaScript.

**A note on coding:** We don't presume that you are entering this class with knowledge of writing HTML, JavaScript, or CSS, or that you have much coding experience at all! However, it's important in this course to have some experience with how our modern UI systems are constructed. As the first activity of this type in the class, this one is probably the most difficult. This assignment is completable (and has been completed) by students with no prior programming experience. If you get stuck, ask for help and don't give up!

**A second note on coding:** Students are coming into this class with a very wide range of programming experience. We will focus on coding tasks that are necessary to cover the course material. For most assignments, I will provide extra activities and challenges for students who have a stronger tech background.

## Why do we use HTML in this class?

- It's the easiest way to build user interfaces that work across  device platforms (Mac, Linux, Windows, Android, iOS). Although HTML was originally intended for web documents, it is often used for desktop and mobile applications.
- We can create our interfaces using a text editor, and don't need any fancy development tools.
- Web apps are very easy to distribute. We'll use the (free) [Github Pages](http://pages.github.com) service to host our apps.
- Increasingly, many popular apps are written in HTML, including [Slack](http://slack.com), [Atom](http://atom.io), and [WhatsApp](http://www.whatsapp.com).

For this assignment, we will be developing the UI structure for our prototype and using JavaScript to add simple interactive behaviors, like switching UI tabs. We won't be programming the "back end" code that controls the logic of our application, although you could certainly do that part too if you wanted.

## What you will need

- A text editor. You can use whatever text editor is installed on your system - Notepad on Windows, TextEdit on Mac, vim, etc. Later you may want to upgrade to a text editor with more features. [VSCode](https://code.visualstudio.com) and [Atom](http://atom.io) are good, cross-platform solutions, and they are both written in HTML/CSS/JavaScript!
- A local folder to store your files. We'll be doing a bunch of these assignments, so you might want to create an "assignment1" folder for this one.
- A GitHub account. GitHub is a service for hosting program source code.  We'll be using [Github Pages](http://pages.github.com) to host our code, as it's free and relatively convenient (and because the university no longer provides convenient web hosting). It's free, and if you sign up via [Github Education](https://education.github.com) you will get a bunch of other free stuff.

## Useful reference materials

Before we start, it's a really good idea to load up some reference pages in case you run into something you don't know how to do. Here are a few useful references for HTML, CSS, and JavaScript:

- [HTML basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) and [next steps](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
- [CSS basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics) and [next steps](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS)
- [JavaScript basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics) and [JQuery fundamentals](http://jqfundamentals.com/chapter/javascript-basics)

We'll be using a code library, [JQuery](https://api.jquery.com), to make our work a little easier. JQuery is mostly useful for reducing the amount of code that we need to write, and letting us do more with less code. We can link to JQuery directly from our code, so you don't need to download or install it.

## What you'll do

In this assignment, we will be creating a simpler phone dialer application, similar to the iOS and Android Phone apps. A demo version of the app is shown below. 

The general idea is to create a three-tab user interface. Tab 1 has a dialer interface with a phone-style keypad, a text field, and buttons to dial and clear the text field. Tab 2 has a list of contacts. Tab 3 has a form for adding contacts: a field for name, phone, and email, and buttons to add the contact or clear the form.

![animated image shows switching between tabs](images/tabs.gif)

For this particular assignment, we will be writing the HTML code that represents the user interface structure, writing some CSS code to adjust the presentation of that interface, and writing JavaScript code to handle the tab switching. All of this code runs right in the browser itself, so there's no code on the server or anything else. 

In the future, if you wanted to make this into a "real" desktop application, you could write code that runs on a web server, or in a standalone application (using [Electron](http://electronjs.org)). We won't do that now but you will have opportunities to do so later.

Right now, we are not going to add in all the accessibility features that we could add. Over the next few weeks, we will extend this prototype to add more features, including accessibility features.

## Some advice before you start

Completing this assignment will probably involve learning some new coding techniques, including some HTML, CSS, and JavaScript. If you know those already, you still may need to learn about how to use new libraries or techniques.

Example code to do all of these things is available online. However, I stronglt encourage you not to complete this assignment by just copying code from the web, or from someone else in the class. Once you learn how these this setup works, it will be much easier to build on that knowledge as we go through the course. It's very tempting, and common, to hack some code together for the first assignment, only to get stuck later when we add on to this project. 

**My advice for this particular assignment is to write out all the code by hand, and to not copy and paste anything.** Even if you get help from someone else or look something up on Google, it's worth your time to re-type the code and see what's in it. Later on, it will be easier to copy and paste things to put something together more quickly, but for now, it will help your understanding if you put the code together yourself piece by piece.

If you get stuck, I am happy to help, but I'll ask you to talk to me about what you're attempting to do and what you've tried already. You can also ask others for help. Just remember that if you're stuck on something, the important thing to do is to figure out why something isn't working, and how it's supposed to work. Getting help on what a specific line of code should be, without understanding why it is that way, is just going to cause you future problems.

## Step-by-step instructions

### Step 1: Create your files
We will create three text files that comprise your app:

1. *index.html* - this HTML file will contain the underlying structure of the user interface. In this file, you will write code that represents the three UI tabs and their contents. All three tabs will go in a single file; we'll use JavaScript to control which tab is visible at a given time.

	We will annotate our HTML document with *classes*, which indicate a certain type of element in our user interface (such as buttons on the tab bar), and *IDs*, which indicate specific items in our user interface (such as the "Dial" button).  
2. *phone.css* - this CSS file tells the web browser how to render the given web page: for example, how big buttons are, and where they appear on the screen. Our CSS file consists of a list of rules, and refers to the styles and IDs in the HTML file so that we can, for example, change the appearance of buttons in the tab bar without changing all of the buttons.

	The cool thing about the CSS file is that it allows us to change the presentation of our UI without changing the HTML code - for example, to create a "high contrast" version of our UI, we only need to change the CSS file. This will be useful later.
	
3. *phone.js* - this file will contain JavaScript code that controls our user interface. We will write code to hide the inactive user interface tabs, and to show the appropriate tab when the user clicks on the tab.

To give you a sense of how much code we'll be producing for this assignment, for my version of this project, there are about 80 lines of HTML, 20 lines of CSS, and 50 lines of JavaScript.

### Step 2: Create a blank HTML page

Edit your index.html file. Every HTML document has the same basic structure, which we will add on to as we go.

Here is what your basic HTML page will look like. (Again, I beg you to go through this and write it up yourself rather than just copy and pasting, so you will get some practice in structuring HTML documents).

```html
<html>
  <head>
    <title>Your Page Title</title>
  </head>
  <body>
    Your page content.
  </body>
</html>
```

As you can see, HTML consists of a series of nested "tags". Over time you will learn what most of the tags do. Many of the tags have both a starting tag, like ```<html>```, and an ending tag, like ```</html>```. Everything inside it is, you guessed it, the HTML document.

Everything that is rendered as part of the HTML document, and our user interface, will be placed within the body tags.

### Step 3: Getting to know our HTML tags

HTML has a whole bunch of tags. For creating our user interface, we are going to use a relatively small subset of the tags. For this activity, we will be using the following tags - although you are free to use others.

- ```<div class="className" id="idName"></div>``` - The div tag represents a section in the document or user interface. For example, we would use a separate div tag for each of the user interface tabs.

	You'll notice that the example div tag has both a class name and an id. For this assignment, you should choose class names and ids for each of your elements. The class represents the type of the UI element - such as a tab bar, tab content, etc. Multiple tags can have the same class, and each tag can have multiple classes, separated by a space. The id represents a unique identifier for a specific item, which we can use to style that element or control it via JavaScript code.
	
	The content of the tab is between the two ```<div></div>``` tags. In the project of the example shown above, we use a ```div``` for each tab of the user interface.
	
- ```<button class="className" id="idName">Button label</button>``` - These are buttons. We must give the button an id if we want to be able to respond to clicks, so it is good practice to give each button an ID.

- ```<input class="className" id="idName"/>``` - this represents a text box. In general, we will place inputs within a ```<form>``` tag, and will add an accompanying label tag to label the form.
	
	For example, the following code snippet describes a form with a single input and a label for that input.
	
```
<form>
  <label for="name">Name</label>
  <input id="name" placeholder="Jane Smith">
</form>
```

By using these tags, we can create the interface shown in the above image. You may use other tags, and over time you will learn more as needed.

### Step 4: AddingJQuery

In your HTML page, you will add references to import the JQuery library. For now, we will copy these tags directly into your document and link to a remote copy of the JQuery library, although we could also download a local copy and link to that.

To import the JQuery JavaScript library, add the following tag. For reasons that aren't important now, you should add this tag to the end of your HTML body, i.e., before the closing ```</body>``` tag:

```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
```

You also need to add references in your HTML document to the CSS and JS files that you are creating. Put them in the same place that you placed the other Pure CSS and JQuery tags above.

In the document head:

```<link rel="stylesheet" href="phone.css">```

At the end of the document body:

```<script src="phone.js"></script>```

### Step 5: Set up the structure of your app

Next, you should focus on writing the HTML code to represent your document. Don't worry about how it looks now; we'll fix that later. Also, at the start, all three tabs will be visible on the screen at once. We'll fix that in the next step.

There are many ways to structure your document, but here is one good way to do it:

- At the top of your body, create a ```<div>``` tag with an id of "tab_bar" or something like that. Inside that tag, add three buttons, one for each of the UI tab buttons. Each button needs an id so we can wire them up to our JavaScript code later.
- After the tab bar, create another ```<div>``` tab with an id of "content" or something similar. This div will contain the content of the three tabs (i.e., the phone dialer interface, the add contact interface)
- Inside the content div, create three other divs. These will represent the three tab "screens". Give them ids that represent their content, like "content_dialer" and "content_list". Naming your UI elements in a sensible way will save you a lot of trouble later.

You don't need to exactly follow the demo app we created, but your app should have all he same elements. Once you have set up your HTML code, you are done with the HTML part of this activity, and shouldn't need to touch the HTML again.

### Step 6: Add JavaScript code to control the user interface

In the phone.js file, you will add code to do control the interactive parts of the user interface. For this assignment, we will mainly use JQuery's [show](http://api.jquery.com/show/) and [hide](http://api.jquery.com/hide/) functions to hide the non-active tabs.

JavaScript syntax is pretty complicated, so we'll give you a starting point here. This code should go into your JavaScript file.

```
$(document).ready(function() { // do this when the document is loaded
	$("#element").show(); // show the element with ID "element"
	$("#otherElement").hide(); // hide the element with ID "otherElement"
});
```
This code will run each time your page is loaded. You will need to customize this code to hide all others but the default tab.

Note that we will often use the JQuery code block ```$("#x")``` to mean *do something to the HTML tag with ID 'x'.*

After you have completed this task, and the page shows only the first tag, you will need to write additional code to handle the other tabs. When a tab button is clicked, the corresponding tab is shown and the others are hidden. Here is an example to get you started.

```
$("#button_id").click(function() { // when "button_id" is clicked
	$("#element").show(); // show element
	$("#other_element").hide();	// hide other element
});
```

Again, you will need to customize this code for your specific project.

### Step 7: Add styles to control the representation of your buttons

You can add content to your .css file to change the appearance of your HTML. You can do this to change button sizes, change spacing, change colors, etc. The CSS file consists of a series of "selectors" that reference some part of your HTML document, and a set of attributes that will then be applied to those elements.

In general, you will use the class names and id names in your HTML documents in your CSS file. This is why it's important to give your elements class names and id names. In CSS, ".className" refers to all elements with that class name, and "#idName" refers to the single element with that ID name.

We could spend weeks exploring the intricacies of HTML. For now, we'll start with some simple examples. Here are a few examples that could be used in this project. You can read the [CSS basics document](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics) for next steps.

```
/* make all buttons 20 by 20 pixels with white text and green background and a 10 pixel margin */
button { width: 20px; height: 20px; background: green; color: white; margin: 10px; }

/* make all tags with the "cool" class name have blue text */
.cool { color: blue; }

/* make the button with ID "delete" red */
#delete { background: red; }
```

The goal for this step is to do something interesting with your file - you can copy the design from the demo, or make something your own.

### Step 8: Publish your files

You will post your three files (html, css, and js) on [GitHub Pages](http://pages.github.com). That page contains step-by-step instructions for posting your files. If you don't want to use the GitHub program, you can create files using the GitHub web interface and paste the contents of your local files in.

Note that once you post your HTML files, there will be two web addresses for your code: a link to your source code on Github, and a link to the hosted web page. For example, for my personal web site, [https://github.com/shaunkane/shaunkane.github.io] links to the source code, but [http://shaunkane.github.io] goes to the page itself. You will need to share the URL of the posted files, not the source code repository. The Settings page on your Github repository will contain this information.

## What to turn in

All you need to turn in is the URL for your prototype. Make sure to test it to make sure it works properly.