# React refrences
> 1. Hooks: https://www.w3schools.com/react/react_hooks.asp
> 2. lifecycle: https://www.w3schools.com/react/react_lifecycle.asp
> 3. axios: https://axios-http.com/docs/api_intro
> 4. interview: https://www.interviewbit.com/react-interview-questions/

# Revision Questions

> 1. What is React

React is a front-end and open-source JavaScript library which is useful in developing user interfaces specifically for applications with a single page. It is helpful in building complex and reusable user interface(UI) components of mobile and web applications as it follows the component-based approach.

Component-based: React applications are built using reusable components, which are like small independent building blocks. You can create components for things like buttons, menus, or even entire pages. This makes it easier to build complex UIs and maintain your code.

Efficient updates: React uses a virtual DOM to efficiently update the real DOM. This means that when your data changes, React only updates the parts of the UI that actually need to be changed. This makes your applications faster and more responsive.

> 2. React advantages

Improved Performance: The virtual DOM and efficient update process lead to faster and more responsive web applications.

Enhanced Developer Experience: React's component-based structure and declarative style promote cleaner and more maintainable code, making development smoother.

Reusable Components: Components can be reused throughout your application, saving development time and effort.

Large Community and Ecosystem: React has a vast and active community that provides extensive documentation, tutorials, and a wide range of third-party libraries and tools, simplifying development and offering numerous solutions.

SEO-friendliness: SEO is about making it easier for developers to find the right content for the user. When a user makes a search, search engines platforms like Google, Yahoo, Bing or Baidu try to find which page is the most relevant to that specific search. React affects the SEO by giving you a SPA (Single Page Application) which requires Javascript to show the content on the page which can then be rendered and indexed.

> 3. What are features of react

React boasts several features that make it a powerful tool for building UIs. Here are some of the key ones:

Components: React.js divides the web page into multiple components as it is component-based. Each component is a part of the UI design which has its own logic and design

JSX (JavaScript Syntax Extension): JSX is an optional syntax extension for JavaScript that allows you to write HTML-like code within your JavaScript. This makes it easier to write code that describes the UI.

Virtual DOM: React uses a virtual DOM, a lightweight representation of the real DOM. When the data in your application changes, React efficiently updates the virtual DOM and then determines the minimal changes needed in the actual DOM. This significantly improves performance.

One-way Data Binding: React follows a one-way data flow. Data is passed down from parent components to child components as props. This predictability makes reasoning about your application's state easier.

State and Props: Components can have internal state to manage their data and props to receive data from parent components. This allows components to be flexible and reusable.

Performance: React's virtual DOM and one-way data binding contribute to its performance optimizations. It only updates the necessary parts of the UI when data changes, leading to a smoother user experience.

Simplicity: React's focus on components and declarative UI definition makes it relatively easy to learn and use, especially for developers familiar with JavaScript.

> 4. What is JSX

JSX stands for JavaScript XML. It's a syntax extension for JavaScript that allows you to write HTML-like code within your React components. While not required for using React, JSX is widely adopted by React developers due to several benefits

> 5. What is virtual dom and actual dom explain difference and how work togather

Imagine you have a complex blueprint for a building (the Actual DOM) and a smaller, more manageable copy of that blueprint (the Virtual DOM). That's essentially the relationship between the Virtual DOM and the Actual DOM in React applications.

Actual DOM (Document Object Model):\
The real representation of the web page structure in the browser.
It's a tree-like structure where elements like `<div>`, `<p>`, etc. are nodes.
Modifying the Actual DOM can be slow and resource-intensive, especially for frequent updates.
	
Virtual DOM:\
A lightweight in-memory representation of the Actual DOM.
It's a JavaScript object that mirrors the structure of the Actual DOM.
When changes are made to the UI in React, they are reflected in the Virtual DOM first.
React compares the updated Virtual DOM with the previous version to determine the most efficient way to update the Actual DOM.
	
How they work together:

Changes in React Components: When you make changes to the state or props of a React component, React reflects those changes in the Virtual DOM.\
Virtual DOM Diffing: React performs a diffing process to compare the new Virtual DOM with the previous one. This efficiently identifies the minimal changes required in the Actual DOM.\
Actual DOM Updates: React updates only the necessary parts of the Actual DOM based on the diffing results. This minimizes browser manipulations and improves performance.
	
Benefits of Virtual DOM:

Faster Updates: By only updating the necessary parts of the Actual DOM, React avoids unnecessary re-renders, leading to a smoother and more responsive user experience.
Improved Performance: The Virtual DOM diffing is much faster than directly manipulating the Actual DOM, especially for complex UIs.\
Batching Updates: React can batch multiple Virtual DOM updates together before applying them to the Actual DOM, further enhancing performance.

> 6. what is state and prop and what is the difference between state and props

state and props are the building blocks of managing data and communication between components. They work together to build dynamic and interactive UIs.

State: Imagine state as the internal memory of a component. It holds data specific to that component that can change over time. This data is used to control the component's dynamic behavior. 

Props: Props act like arguments passed to a function. They are read-only data passed down from parent components to their child components. This data is used to customize the child component's behavior or appearance. 

> 7.  what is a  diffrent between class based component and function based component in react

React offers two main approaches for building components: class-based components and functional components. While both can achieve the same outcome, they differ in syntax, structure, and capabilities. Here's a breakdown of the key differences:

Class-based Components:

Definition: Created using the React.Component class as a base.\
Structure: Defined with a render method that returns the JSX representing the UI. Can also have additional lifecycle methods for handling various stages of a component's existence (e.g., componentDidMount, componentWillUnmount).\
State Management: Can manage internal state using the this.state object and the setState method to update the state and trigger re-renders.\
Complexity: Generally considered more complex due to the class syntax and lifecycle methods.

Functional Components:

Definition: Defined as simple JavaScript functions that accept props as arguments and return JSX representing the UI.\
Structure: Simpler syntax compared to class components. No lifecycle methods by default (introduced in React 16.8 with Hooks).\
State Management: Traditionally, functional components could not manage state on their own. However, with the introduction of Hooks (useState, useEffect, etc.), functional components can now manage state and perform side effects.\
Complexity: Generally considered easier to understand and use due to their simpler syntax.
	
Both class-based and functional components are valid approaches in React. Class components offer more built-in functionality for state management and lifecycles, while functional components with Hooks provide a simpler and more modern way to achieve similar results. The choice often depends on project requirements, developer preference, and familiarity with Hooks.

> 8.  What is React Fragments

React Fragments are a way to group multiple JSX elements together without adding an extra DOM node. In React, when you return multiple elements from a component's render function, it implicitly wraps them in a `<div>` element. This can be inconvenient in some scenarios where you don't want that extra parent node cluttering your HTML structure

Syntax: There are two ways to create React Fragments:\
Empty JSX tags: <></> (preferred for readability)\
Fragment component: React.Fragment (less common)

Purpose: React Fragments allow you to return a list of JSX elements without introducing an unnecessary parent element in the DOM. Keeping your HTML structure clean and avoiding unnecessary nesting.

> 9. Differentiate between stateful and stateless components

In React.js, components are the building blocks for your user interfaces. They determine how data is displayed and how users interact with your application. But there are two main categories of components that differ in how they manage data and update the UI: stateful and stateless components.

Stateful Components:

Internal Data Management: Stateful components can manage their own data using a concept called state. This state is like a component's memory, and it can change over time in response to user interactions or other events.

Dynamic Behavior: They are ideal for situations where the UI needs to update based on changes in the component's state. This makes them suitable for handling things like user input forms, interactive features, or components that display data fetched from an API.

Re-rendering on State Change: Whenever the state of a stateful component changes, the entire component and its children will re-render to reflect the updated data in the UI.

Implementation: Traditionally, stateful components were created using React's class component syntax. These classes would have a state property to hold the data and methods (like setState) to update it. However, modern React also allows creating stateful components using functional components with Hooks (like useState).

Stateless Components:

Data Reliance on Props: Stateless components, also commonly referred to as presentational components, rely on external data passed down from parent components through props. They don't have their own internal state to manage.

Static UI Presentation: These components are primarily focused on displaying UI elements based on the props they receive. They act as a way to structure and present your application's data visually.

Re-rendering on Prop Change: Stateless components only re-render if the props they receive from their parent component change. Since they don't have their own state, there's no internal data to trigger a re-render on their own.

Implementation: Stateless components are typically written as simpler functional components that accept props as arguments and return JSX (JavaScript XML syntax) to define the UI structure.

> 10. what is axios

Axios is used to communicate with the backend and it also supports the Promise API that is native to JS ES6. It is a library which is used to make requests to an API, return data from the API, and then do things with that data in our React application.

> 11. what is arrow function and how its diffrent from normal javascript function

An arrow function is a shorthand syntax for writing functions in JavaScript. It provides a more concise way to define functions compared to traditional function expressions.

Syntax:\
Arrow functions use a concise syntax with an arrow (=>) between the parameter list and the function body.
Traditional functions use the function keyword and have a more verbose syntax.

this Binding:\
Arrow functions do not have their own this context. Instead, they inherit the this value from the enclosing lexical scope (i.e., the context in which they were defined).
Traditional functions have their own this context, which can vary depending on how the function is called (e.g., as a method, as a standalone function, or with call or apply).

arguments Object:\
Arrow functions do not have their own arguments object. If you need to access arguments, you can use the rest parameter syntax (...args).
Traditional functions have an arguments object that contains all the arguments passed to the function.

new Operator:\
Arrow functions cannot be used as constructors. They do not have a prototype property and cannot be called with the new operator.
Traditional functions can be used as constructors to create new instances of objects using the new operator.

super keyword:\
Arrow functions do not have their own super binding, which means they cannot be used as methods in classes that use inheritance.
Traditional functions can use the super keyword to access methods and properties of an object's parent.
In general, arrow functions are often preferred for their concise syntax and lexical scoping behavior, especially for simple, short functions and when you want to maintain the lexical this context. However, traditional functions still have their place, particularly when you need the this binding to be dynamic or when you need the arguments object.

> 12. diffrent between useMemo and useCallback

The useMemo and useCallback Hooks are similar. The main difference is that useMemo returns a memoized value and useCallback returns a memoized function.
	
> 13.  what is strict mode

Strict mode is a development mode only feature for highlighting potential problems in an application. It helps to identify unsafe lifecycles, legacy API usage, and a number of other features.Strict mode can be enabled for any part of your application, but it is especially useful to use while developing new codes or debugging the application.

> 14. What are Higher Order Components

In React, higher-order components (HOCs) are a way to reuse component logic. They are functions that take an existing component and return a new component with added functionality. This is similar to higher-order functions in JavaScript, which take functions as arguments and return new functions.

Here are some key points about HOCs:

Purpose: Promote code reuse by encapsulating common functionalities in a separate component. This can improve code organization and maintainability.\
How it works: An HOC takes a component as input and returns a new component that wraps the original component. The HOC can inject additional logic or props into the wrapped component.\
Use cases: Common use cases for HOCs include adding authentication, authorization, data fetching, state management, or styling to multiple components.\
While HOCs were previously a common technique in React, it's important to note that React's API has evolved and there are often better ways to achieve the same functionality using techniques like hooks and context API. However, HOCs are still a valuable concept to understand, especially if you encounter them in existing codebases or third-party libraries.

> 15. what is lifecycle in react and explain react lifecycle

https://www.w3schools.com/react/react_lifecycle.asp

In React, the term "lifecycle" refers to the series of events or phases that a React component goes through from its initialization to its destruction. Understanding the React component lifecycle is crucial for managing state, performing side effects, and optimizing performance in React applications.

> 16.  Explain about types of Hooks in React

Built-in Hooks: The built-in Hooks are divided into 2 parts as given below:

https://www.w3schools.com/react/react_hooks.asp

Basic Hooks:

useState(): This functional component is used to set and retrieve the state.\
useEffect(): It enables for performing the side effects in the functional components.\
useContext(): It is used for creating common data that is to be accessed by the components hierarchy without having to pass the props down to each level.

Additional Hooks:

useReducer() : It is used when there is a complex state logic that is having several sub-values or when the upcoming state is dependent on the previous state. It will also enable you to optimization of component performance that will trigger deeper updates as it is permitted to pass the dispatch down instead of callbacks.\
useMemo() : This will be used for recomputing the memoized value when there is a change in one of the dependencies. This optimization will help for avoiding expensive calculations on each render.\
useCallback() : This is useful while passing callbacks into the optimized child components and depends on the equality of reference for the prevention of unneeded renders.\
useImperativeHandle():  It will enable modifying the instance that will be passed with the ref object.\
useDebugValue(): It is used for displaying a label for custom hooks in React DevTools.\
useRef() : It will permit creating a reference to the DOM element directly within the functional component.\
useLayoutEffect(): It is used for the reading layout from the DOM and re-rendering synchronously.

Custom Hooks:

A custom Hook is basically a function of JavaScript. The Custom Hook working is similar to a regular function. The “use” at the beginning of the Custom Hook Name is required for React to understand that this is a custom Hook and also it will describe that this specific function follows the rules of Hooks. Moreover, developing custom Hooks will enable you for extracting component logic from within reusable functions.


> 17.  What is React Router?

React Router refers to the standard library used for routing in React. It permits us for building a single-page web application in React with navigation without even refreshing the page when the user navigates. It also allows to change the browser URL and will keep the user interface in sync with the URL. React Router will make use of the component structure for calling the components, using which appropriate information can be shown. Since React is a component-based framework, it’s not necessary to include and use this package. Any other compatible routing library would also work with React.

The major components of React Router are given below:

BrowserRouter: It is a router implementation that will make use of the HTML5 history API (pushState, popstate, and event replaceState) for keeping your UI to be in sync with the URL. It is the parent component useful in storing all other components.

Routes: It is a newer component that has been introduced in the React v6 and an upgrade of the component.

Route: It is considered to be a conditionally shown component and some UI will be rendered by this whenever there is a match between its path and the current URL.

Link: It is useful in creating links to various routes and implementing navigation all over the application. It works similarly to the anchor tag in HTML.