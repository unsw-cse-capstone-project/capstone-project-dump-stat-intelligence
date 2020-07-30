import "../styles/styles.scss";

import App from "next/app";
import React, { useEffect } from "react";
import { Provider, useDispatch, useSelector } from "react-redux";
import { createWrapper } from "next-redux-wrapper";
import store from "../lib/redux/store";
import { useRouter } from "next/router";

import Head from "next/head";
import Nav from "../components/nav/Nav";
import PantryButton from "../components/Pantry/PantryButton";
import EditButton from "../components/creator/EditButton";

import { attemptLoginFromLocalStorage } from "../lib/redux/actions/authAction";
import { get_pantry } from "../lib/redux/actions/pantryAction";

function PantryPirate({ Component, pageProps }) {
  const router = useRouter();
  const dispatch = useDispatch();
  const isLoggedIn = useSelector(state => state.auth.isLoggedIn);

  useEffect(() => {
    dispatch(attemptLoginFromLocalStorage())
    .then(res => {
      if (res) {
        setTimeout(() => {dispatch(get_pantry())}, 50);
      }
    });
  }, []);

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
        {router.pathname == "/recipe/create" ? (
          <EditButton />
        ) : (
          isLoggedIn ? <PantryButton /> : ""
        )}
      </main>
    </Provider>
  );
}

const makestore = () => store;
const wrapper = createWrapper(makestore);

export default wrapper.withRedux(PantryPirate);
