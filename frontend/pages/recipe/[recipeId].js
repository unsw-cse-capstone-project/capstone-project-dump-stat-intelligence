import Head from "next/head";
import { useRouter } from "next/router";

import RecipeAPI from "../../lib/api/recipe";

function Recipe(props) {
  console.log(props);
  return (
    <div>
      <Head>
        <title>Pantry Pirate | Create</title>
      </Head>
      <div className="container">
        <div className="columns is-centered">
          <div className="box column is-6">
            <h1 className="title">{props.name}</h1>
            <p>
              Author: {props.author.username} | Cook time: {props.cook_time}
            </p>
            <p>{props.method}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

Recipe.getInitialProps = async ({ query: { recipeId } }) => {
  const { data } = await RecipeAPI.get(recipeId);

  return data;
};

export default Recipe;
