#include <time.h>
#include <stdlib.h>

#include "whoiMath.h"

#include <gtest/gtest.h>

const int N_TRIALS = 1000;

float trusted_divide(const float &a, const float &b){
  return a * (1.0 / b);
}

float trusted_divide(const int &a, const int &b) {
  return trusted_divide((float)a, (float)b);
}


class WhoiMathDivideTests: public testing::Test {
  protected:
    virtual void SetUp() {
      whoiMath = new WhoiMath();
    }

    virtual void TearDown() {
      delete whoiMath;
    }

    WhoiMath *whoiMath;
};

TEST_F(WhoiMathDivideTests, ZeroIdentity){
  EXPECT_EQ(whoiMath->divide(0, 5), 0);
}

TEST_F(WhoiMathDivideTests, Identity){
  EXPECT_EQ(whoiMath->divide(5, 1), 5);
}

TEST_F(WhoiMathDivideTests, IntegerDivision) {
  EXPECT_EQ(whoiMath->divide(5, 3), trusted_divide(5, 3));
}

TEST_F(WhoiMathDivideTests, FloatDivision) {
  for(int i=0;i<N_TRIALS;i++){
    const int a = rand();
    const int b = rand();
    EXPECT_EQ(whoiMath->divide(a, b), trusted_divide(a, b));
  }
}


int main(int argc, char** argv) {
  // Disables elapsed time by default.
  // ::testing::GTEST_FLAG(print_time) = false;

  // This allows the user to override the flag on the command line.
  ::testing::InitGoogleTest(&argc, argv);

  int test_return = RUN_ALL_TESTS();

  return test_return;
}
