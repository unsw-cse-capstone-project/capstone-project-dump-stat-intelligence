import Head from "next/head";
import React from "react";

import RecipeAPI from "../lib/api/recipe";

import { useSelector } from 'react-redux'; 
import RecipeCard from "../components/RecipeCard/RecipeCard";

function Explore(props) {
  console.log(props.results);
  return (
    <>
      <Head>
        <title>Pantry Pirate | Explore</title>
      </Head>
      <div>
        <br />
        <h1 className="title is-2">Explore Recipes</h1>
        <div className="columns is-multiline">
          {props.results ? (
            props.results.map((recipe, idx) => (
              <div key={idx} className="column is-3">
                <RecipeCard
                  className="column is-3"
                  src={`https://source.unsplash.com/400x300/?food&sig=${recipe.id}`}
                  title={recipe.name}
                  id={recipe.id} // TODO: alter
                />
              </div>
            ))
          ) : (
            <p>Loading...</p>
          )}
        </div>
      </div>
    </>
  );
}

Explore.getInitialProps = async ({ req }) => {
  const { data } = await RecipeAPI.getAll();
  console.log(data);

  return { results: data };
};

export default Explore;
