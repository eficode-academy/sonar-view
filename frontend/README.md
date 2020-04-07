# Eficode Sonar Frontned

### Project setup

To set up this project on your compoter you need to have `nodejs` and `npm` or `yarn` installed on your computer.

First install the dependencies in the root of the frontend directory

<pre>npm install</pre>

or if you prefere `yarn`

<pre>yarn install</pre>

Run the application in the development mode by running

<pre>npm run dev</pre>

or

<pre>yarn dev </pre>

The project will run on port `3000`

### Project structure

In the project, the code lives in the `src` directry. The code that in the `components` folder are dummy components, as in, they do not contain any actual data. `Containers` on the other hand are components that contain data.

`Rebass` and `styled components` are used to styling of the project. Theming happens in the `utils/theme.js`. No colors or font sizes are to be defined outside of the `theme.js`

#### Responsive layout

`theme.js` contains a media query property. By calling `theme.media` you can access the various media queries. For example while using styled components, media queries can be called as such:

```js

const StyledDiv = styled.div `
    color: red;
    display: block;
    ${(props) => props.theme.media.md`
        display: none
    `
`
```
