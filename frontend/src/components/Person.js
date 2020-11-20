import React from "react";
import { Box, Flex, Text } from "rebass";
import { withRouter } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import PropTypes from "prop-types";
import useDataLoader from "../hooks/useDataLoader";
import theme from "../utils/theme";

function Person({ match }) {
  const { email, date } = match.params;
  const { personDetails = [], isLoading } = useDataLoader(
    `surveys/${date}/persons/${email}`,
    "DETAILS",
    "personDetails",
  );

  const PROFICIENCY_LEVELS = 5;
  const levels = {
    "fundamental awareness": 1,
    novice: 2,
    intermediate: 3,
    advanced: 4,
    expert: 5,
  };

  if (isLoading) 
    return <div>Loading...</div>;

  if (!isLoading) {
    return (
      <>
      <Flex
        p={["30px", "60px"]}
        width={["94%", "94%", "94%", "60%"]}
        justifyContent={["space-between"]}
        alignItems="center"
        flexWrap="wrap"
        sx={{ border: `1px solid ${theme.colors.lightGrey}` }}
        fontSize="14px"
      >
        <Box>
          <FontAwesomeIcon icon={faUser} size="7x" />
        </Box>
        <Box pt={["10px", 0]}>
          <Text>
            Name:
            {personDetails[email]?.name}
          </Text>
          <Text>
            Email:
            {personDetails[email]?.email}
          </Text>
          <Text>
            Office:
            {personDetails[email]?.office}
          </Text>
          <Text>
            Team:
            {personDetails[email]?.team}
          </Text>
        </Box>
        <Box width="100%" mt="30px">
          {personDetails[email]?.survey.map((s) => (
            <Flex key={s.name} my="10px" alignItems="center">
              <Box width="30%">
                <Text>
                  {s.name}
                  {' '}
                </Text>
              </Box>
              <Box
                ml="30px"
                bg="white"
                width="70%"
                sx={{ border: `1px solid ${theme.colors.lightGrey}` }}
              >
                <Box
                  p="6px"
                  bg={theme.colors.green}
                  width={levels[s.level.toLowerCase()] / PROFICIENCY_LEVELS}
                  height="25px"
                />
              </Box>
            </Flex>
          ))}
        </Box>
      </Flex>
      </>
    );
  }
}

Person.propTypes = {
  match: PropTypes.shape({
    params: PropTypes.shape({
      email: PropTypes.string,
      date: PropTypes.string,
    }),
  }).isRequired,
};

export default withRouter(Person);
