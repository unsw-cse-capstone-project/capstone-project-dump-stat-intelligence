import Head from "next/head";
import React from "react";

import { useSelector, useDispatch } from "react-redux";
import { update_create } from "../../lib/redux/actions/createAction";

export default function Create(props) {
  const dispatch = useDispatch();
  let edit = useSelector(state => state.create);
  function partialUpdate(event, cat) {
    dispatch(update_create(cat, event.target.value));
  }
  return (
    <>
      <Head>
        <title>Pantry Pirate | Create</title>
      </Head>
      <div className="container">
        <div className="columns is-centered">
          <div className="box column is-10">
            <h1 className="title">Recipe preview</h1>
            

            <div className="buttons">
              <button className="button is-light is-success">
                Add Recipe
              </button>
              <button className="button is-light is-danger">Discard</button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

