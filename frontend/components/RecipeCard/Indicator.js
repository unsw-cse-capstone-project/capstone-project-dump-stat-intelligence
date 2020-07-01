import styles from "./RecipeCard.module.scss";

import React from "react";

export default class Indicator extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hover: false };
  }
  render() {
    return (
      <div
        onMouseOver={() => this.setState({ hover: true })}
        onMouseLeave={() => this.setState({ hover: false })}
        className={styles.indicator}
      >
        {!this.state.hover ? (
          this.props.value
        ) : (
          <div className={styles.indicator.open}>{this.props.children}</div>
        )}
      </div>
    );
  }
}