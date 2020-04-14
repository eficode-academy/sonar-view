# Eficode Sonar Frontend

### Project setup

To set up this project on your computer you need to have [node.js](https://nodejs.org/) and `npm` or [yarn](https://yarnpkg.com/) installed on your computer.

This project uses [React](https://reactjs.org/)

To run the project locally, first install the dependencies while in the root of the frontend directory

```sh
npm install
```

or if you prefere `yarn`:

```sh
yarn install
```

Run the application in the development mode by running the command:

```sh
npm run dev
```

or

```sh
yarn dev
```

The project will run on port `3000`

### Project structure

In the project, the code lives in the `src` directry. The components in the `components` folder are dummy components, as in, they do not contain any actual data. `containers` on the other hand are components that contain data.

[Rebass](https://rebassjs.org/) and [Styled components](https://styled-components.com/) are used to styling of the project. Theming happens in the
[utils/theme.js](./src/utils). No colors or font sizes are to be defined outside of the `theme.js`

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
