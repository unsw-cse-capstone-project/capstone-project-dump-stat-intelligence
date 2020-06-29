import "../styles/styles.scss";

import App from 'next/app';
import React from 'react';
import { Provider } from 'react-redux';
import { createWrapper } from 'next-redux-wrapper';
import store from '../lib/redux/store';

import Head from "next/head";
import Nav from "../components/nav/Nav";
import PantryButton from "../components/Pantry/PantryButton";

class PantryPirate extends App {
  
  render() {
    const { Component, pageProps } = this.props;
    return (
      <Provider store={store}>
        <Head>
          <title>Pantry Pirate</title>
          <meta charSet="utf-8" />
          <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        </Head>
        <Nav />
        <main>
          <div className="container">
            <Component {...pageProps} />
          </div>
          <PantryButton />
        </main>
      </Provider>
    )
  }
}

const makestore = () => store;
const wrapper = createWrapper(makestore);

export default wrapper.withRedux(PantryPirate);
