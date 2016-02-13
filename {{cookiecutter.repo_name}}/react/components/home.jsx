/* global gettext */
var React = require('react');

var Home = React.createClass({
  propTypes: {
    urls: React.PropTypes.object
  },

  render: function () {
    return (
      <div>
        <h1 className="cover-heading">{gettext('It worked!')}</h1>
        <p className="lead">
          {gettext('Congratulations on your first Django-powered page.')}
        </p>
      </div>
    );
  }
});
module.exports = Home;
