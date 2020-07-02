import Head from "next/head";
import { withRouter } from "next/router";
import React from "react";

import RecipeAPI from "../../lib/api/recipe";
import Error from "../../components/Error/Error";

class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      recipe: null,
      error: null,
    };
  }

  componentDidMount() {
    RecipeAPI.get(this.props.router.query.recipeId).then(
      ({ data }) => {
        console.log(data);
        this.setState({ recipe: data, loading: false });
      },
      (err) => {
        console.log(err);
        this.setState({ error: err.response, loading: false });
      }
    );
  }

  handleDelete = async (e) => {
    this.setState({ loading: true });
    const res = await RecipeAPI.delete(this.state.recipe.id, ""); // TODO: token authentication
    console.log(res);
    this.setState({ loading: false });
  };

  render() {
    if (this.state.error) {
      return <Error message={this.state.error.statusText} />;
    }

    if (this.state.loading) {
      return <p>Loading</p>;
    }
    return (
      <div>
        <Head>
          <title>Pantry Pirate | Create</title>
        </Head>
        <div className="container">
          <div className="columns is-centered">
            <div className="box column is-10">
              <h1 className="title is-2">{this.state.recipe.name}</h1>
              <img
                src={`https://source.unsplash.com/1200x600/?${this.state.recipe.name}`}
              />
              <p>
                Author: {this.state.recipe.author.username} | Cook time:{" "}
                {this.state.recipe.cook_time}
              </p>
              <div className="tags">
                {this.state.recipe.diet_req.map((diet, idx) => (
                  <span className="tag" key={idx}>
                    {diet}
                  </span>
                ))}
              </div>
              <div className="buttons">
                <a className="button is-light">Edit</a>
                <a
                  className="button is-light is-danger"
                  onClick={this.handleDelete}
                >
                  Delete
                </a>
              </div>
              <hr />
              <div className="columns">
                <div className="column is-4">
                  <h4 className="title is-4">Ingredients</h4>
                  <ul>
                    {this.state.recipe.ingredients.map((ingredient, idx) => (
                      <li key={idx}>
                        {ingredient.amount} {ingredient.unit}{" "}
                        {ingredient.ingredient.name}
                      </li>
                    ))}
                  </ul>
                </div>
                <div className="column is-6">
                  <h4 className="title is-4">Method</h4>
                  <p>{this.state.recipe.method}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

// You can't use hooks (i.e. useRouter) with a class component in react
export default withRouter(Recipe);
