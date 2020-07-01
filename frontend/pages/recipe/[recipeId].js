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
          <div className="box column is-10">
            <h1 className="title is-2">{props.name}</h1>
            <img src="https://source.unsplash.com/1200x600/?food" />
            <p>
              Author: {props.author.username} | Cook time: {props.cook_time}
            </p>
            <div className="tags">
              {props.diet_req.map((diet, idx) => (
                <span className="tag" key={idx}>
                  {diet}
                </span>
              ))}
            </div>
            <div className="buttons">
              <a className="button is-light">Edit</a>
              <a className="button is-light is-danger">Delete</a>
            </div>
            <hr />
            <div className="columns">
              <div className="column is-4">
                <h4 className="title is-4">Ingredients</h4>
                <ul>
                  {props.ingredients.map((ingredient, idx) => (
                    <li key={idx}>
                      {ingredient.amount} {ingredient.unit}{" "}
                      {ingredient.ingredient}
                    </li>
                  ))}
                </ul>
              </div>
              <div className="column is-6">
                <h4 className="title is-4">Method</h4>
                <p>{props.method}</p>
              </div>
            </div>
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
