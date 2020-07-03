import "../styles/styles.scss";

import App from "next/app";
import React from "react";
import { Provider } from "react-redux";
import { createWrapper } from "next-redux-wrapper";
import store from "../lib/redux/store";

import Head from "next/head";
import Nav from "../components/nav/Nav";
import PantryButton from "../components/Pantry/PantryButton";

class PantryPirate extends App {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
    };
  }

  componentDidMount() {
    if (window.location.hostname == "localhost") {
      this.setState({
        error:
          "Tom's friendly reminder: Chrome is fucked. Don't use localhost. Use 127.0.0.1 to stop CORS from fucking you: https://stackoverflow.com/questions/10883211/deadly-cors-when-http-localhost-is-the-origin",
      });
    }
  }

  render() {
    const { Component, pageProps } = this.props;
    return (
      <Provider store={store}>
        <Head>
          <title>Pantry Pirate</title>
          <meta charSet="utf-8" />
          <meta
            name="viewport"
            content="initial-scale=1.0, width=device-width"
          />
        </Head>
        <Nav />
        <main>
          <div className="container">
            {this.state.error != null ? (
              <div className="notification is-danger">
                <button
                  className="delete"
                  onClick={() => this.setState({ error: null })}
                ></button>
                {this.state.error}
              </div>
            ) : null}
            <Component {...pageProps} />
          </div>
          <PantryButton />
        </main>
      </Provider>
    );
  }
}

const makestore = () => store;
const wrapper = createWrapper(makestore);

export default wrapper.withRedux(PantryPirate);
